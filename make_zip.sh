eval $"source env/bin/activate";
black *.py
pyinstaller -D -F -n main -c "main.py"
cp bicycle_db.sqlite dist/;
zip -r dist_0_4.zip dist/ build/;