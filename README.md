# Fix for the google gif to cli

- To add the fix, you must first install their shit. Tested on kali.

1. ```bash
   sudo apt-get install ffmpeg zlib* libjpeg* python3-setuptools -y
   ```
2. ```bash
   pip3 install --user gif-for-cli
   ```
3. ```bash
   SITE_PACKAGES_DIR=$(python -m site --user-site) && wget -O "$SITE_PACKAGES_DIR/gif_for_cli/execute.py" "https://github.com/pentestfunctions/gif-for-cli-fix/raw/main/execute.py"
   ```

### This will intall the gif-for-cli, then updated the execute.py file appropriately to fix the issue. 

## Now simply run
```
~/.local/bin/gif-for-cli https://media1.tenor.com/m/0Ukb2awHbtkAAAAC/rob-delaney-peter.gif
```
