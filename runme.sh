source /home/rajani_d/File-Format-Converter/ffc-venv/bin/activate
export SRC_BASE_DIR=/home/rajani_d/File-Format-Converter/data/retail_db
export TGT_BASE_DIR=/home/rajani_d/File-Format-Converter/data/retail_demo
export LOG_FILE_PATH=/home/rajani_d/File-Format-Converter/logs/ffc.log
export SCHEMAS_FILE_PATH=/home/rajani_d/File-Format-Converter/data/retail_db/schemas.json

rm -rf $TGT_BASE_DIR
mkdir -p /home/rajani_d/File-Format-Converter/logs
ffconverter
deactivate