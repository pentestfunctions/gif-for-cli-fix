## Fix
import hashlib
import json
import os
from os.path import expanduser

from . import __version__
from .display import display
from .export import export
from .generate import generate
from .generate.utils import process_input_source
from .utils import get_parser, get_output_dirnames


def execute(environ, argv, stdout):
    parser = get_parser(environ)

    args = parser.parse_args(argv)

    input_source = args.input_source

    input_source_file = process_input_source(input_source, args.api_key)

    home_dir = expanduser('~')

    m = hashlib.md5()
    m.update(input_source_file.encode('utf8'))
    input_source_hash = m.hexdigest()

    output_dirnames = get_output_dirnames(
        home_dir,
        __version__,
        input_source_hash,
        args.cols,
        args.rows,
        args.cell_width,
        args.cell_height
    )

    if not os.path.exists(output_dirnames['.']):
        for output_dirname in output_dirnames.values():
            if not os.path.exists(output_dirname):
                os.makedirs(output_dirname)

        generate(
            stdout=stdout,
            input_source=input_source,
            input_source_file=input_source_file,
            cols=args.cols,
            rows=args.rows,
            cell_width=args.cell_width,
            cell_height=args.cell_height,
            output_dirnames=output_dirnames,
            cpu_pool_size=args.cpu_pool_size,
        )

    with open('{}/config.json'.format(output_dirnames['.']), 'r') as f:
        config = json.load(f)

    if config['num_frames'] > 0:
        seconds_per_frame = config['seconds'] / config['num_frames']
    else:
        seconds_per_frame = 0.1

    if args.export_filename:
        export(
            export_filename=args.export_filename,
            display_dirname=output_dirnames[args.display_mode],
            stdout=stdout,
            cell_char=args.cell_char,
            seconds_per_frame=seconds_per_frame,
            cols=args.cols,
            rows=args.rows,
            cell_width=args.cell_width,
            cell_height=args.cell_height,
            cpu_pool_size=args.cpu_pool_size,
            output_dirnames=output_dirnames,
        )
    elif not args.no_display:
        display(
            display_dirname=output_dirnames[args.display_mode],
            stdout=stdout,
            num_loops=args.num_loops,
            cell_char=args.cell_char,
            seconds_per_frame=seconds_per_frame,
        )
