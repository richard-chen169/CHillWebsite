from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os
from werkzeug.utils import secure_filename
import sys




app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt'])



@app.route('/camera', methods=['GET', 'POST'])
def camera():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
		#    flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		#    flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			UPLOAD_FOLDER = '/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/webTelescope/webCamera/config'
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('camera',
									filename=filename))
	return render_template("camera.html")

@app.route('/channels', methods=['GET', 'POST'])
def channels():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
		#    flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		#    flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			UPLOAD_FOLDER = '/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/webTelescope/webCamera/config'
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('channels',
									filename=filename))
	return render_template("channels.html")

@app.route('/optics', methods=['GET', 'POST'])
def optics():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
		#    flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		#    flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			UPLOAD_FOLDER = '/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/webTelescope/webCamera/config'
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('optics',
									filename=filename))
	return render_template("optics.html")


@app.route('/program', methods=['GET', 'POST'])
def program():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
		#    flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		#    flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			UPLOAD_FOLDER = '/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/webTelescope/config'
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('program',
									filename=filename))
	return render_template("program.html")



@app.route('/foregrounds', methods=['GET', 'POST'])
def foregrounds():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
		#    flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		#    flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			UPLOAD_FOLDER = '/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/config'
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('foregrounds',
									filename=filename))
	return render_template("foregrounds.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
        #    flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
        #    flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template("home.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/mapping', methods=['GET', 'POST'])
def mapping():

    os.system("python2.7 /home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/mappingSpeed.py /home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/")
    return render_template("mapping.html")

@app.route('/display', methods = ['GET', 'POST'])
def display():
	reader = open('/home/richard/Documents/fadedtab/sensitivity_calculators/SO_SensitivityCalculator/CHillCalc2/Experiments/webExperiment/webDesign/sensitivity.txt', 'r')
	fileAsArray = []
	for line in reader:
		fileAsArray.append(line)

	fileAsArray = [elem[:len(elem)-2] for elem in fileAsArray]
	return render_template("display.html", someData=fileAsArray)

if __name__ == "__main__":
	app.run(debug=True)
	

