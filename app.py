from flask import Flask, render_template, request
import os

app = Flask(__name__,
            static_folder='static',     # Explicitly set static folder
            static_url_path='/static')  # Ensure correct static URL path

# Set a directory to temporarily save uploaded files
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_files():
    son_file = request.files.get('sonFile')
    father_file = request.files.get('fatherFile')

    if son_file and father_file:
        # Save files to the upload folder
        son_file_path = os.path.join(app.config['UPLOAD_FOLDER'], son_file.filename)
        father_file_path = os.path.join(app.config['UPLOAD_FOLDER'], father_file.filename)

        son_file.save(son_file_path)
        father_file.save(father_file_path)

        # Read the content and store it in variables
        with open(son_file_path, 'r') as f:
            son_content = f.read()
            print("Son's DNA File Content:")
            print(son_content)

        with open(father_file_path, 'r') as f:
            father_content = f.read()
            print("Father's DNA File Content:")
            print(father_content)

        # Store the read data in variables for processing
        son_dna= son_content.strip()  
        father_dna= father_content.strip()

        print("Stored Son's DNA:", son_dna)
        print("Stored Father's DNA:", father_dna)

        # Return success response (this can also return the variables if needed)
        return {"message": "Files uploaded and stored successfully"}, 200
    else:
        return {"error": "Both files are required"}, 400


if __name__ == '__main__':
    app.run(debug=True)
