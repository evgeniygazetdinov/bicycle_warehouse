python3 -m venv env &&
source env/bin/activate && 
pip install -r requerements.txt &&
sudo apt-get install qttools5-dev-tools -y &&
sudo apt install mdbtools -y;
pyinstaller -D -F -n main -c "main_template.py"
