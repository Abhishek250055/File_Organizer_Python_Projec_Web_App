from flask import Flask, redirect, render_template, request
import os
import shutil

app=Flask(__name__)


# path=input("enter path:=")


def manager_file(path):
    
    files=os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension=extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move( path+'/'+file, path+'/'+extension+'/'+file )
        else:
            os.makedirs(path+'/'+extension)
            shutil.move( path+'/'+file, path+'/'+extension+'/'+file )

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        # Get the long URL from the form submission
        doc_url = request.form.get('doc_url')

        # Generate a unique shortened URL
        new_doc = manager_file(doc_url)

        return render_template('index.html', new_doc=new_doc)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)