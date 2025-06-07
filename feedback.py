from flask import Flask,request,render_template 
app=Flask(__name__)#object of the Flask class 
 
@app.route("/") 
def form(): 
    return render_template("ht_11_03_25.html") 
 
@app.route("/submit",methods=["POST"]) 
def submit(): 
    name=request.form.get("name") 
    email=request.form.get("email") 
    feedback=request.form.get("feedback") 
    return f"""Name:{name}; 
    Email: {email} 
    Thank you for your feedback.\n{feedback}""" 
     
if __name__=="__main__": 
    app.run(debug=True)