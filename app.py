from flask import *
app = Flask(__name__, template_folder='templates')
shapeslist = [{'name':'cone',
                  'id':"0",
                   'cost':"250"},
                {'name':'cylinder',
                 'id':"1",
                 'cost':'300'},
                {'name':'cuboid',
                  'id':"2",
                  'cost':'350'}]
@app.route('/showshapes',methods=["POST","GET"])
def shapes(shapelist=shapeslist):
    '''shapeslist = [{'name':'cone',
                  'id':"0",
                   'cost':"250"},
                {'name':'cylinder',
                 'id':"1",
                 'cost':'300'},
                {'name':'cuboid',
                  'id':"2",
                  'cost':'350'}]'''
    coatlist = [{'name': 'iron',
                 'id':"0",
                 'cost':"250"},
                {"name":'gold',
                 'id':"1",
                 'cost':"500"}]
    if request.method == "POST":
        shapeselected=request.form["shapeid"]
        coatselected=request.form["coatid"]
        if shapeselected=="2" and int(coatselected)<len(coatlist):
            percap=coatlist[int(coatselected)]['cost']
            return redirect(url_for("cuboid",percap=percap))
        elif((shapeselected=="1" or shapeselected=="0") and int(coatselected)<len(coatlist)):
            percap=coatlist[int(coatselected)]['cost']
            shape=shapeselected
            return redirect(url_for("cone",percap=percap,shape=shape))
        elif(int(shapeselected)>=len(shapeslist) or int(coatselected)>=len(coatlist)):
            return jsonify("Enter correct values")
    else:
        return render_template("show.html", content1=shapeslist, content2=coatlist)
@app.route('/cubiod/<percap>', methods=["GET","POST"],endpoint='cuboid')
def calculatecuboid(percap):
    if request.method=="POST":
        length=request.form['l']
        breadth=request.form['b']
        height=request.form['h']
        volume=int(length)*int(breadth)*int(height)*int(percap)
        return jsonify("cost of making cubiodical trophy  :"+str(int(volume)))
    else:
        return render_template("cubiod.html")
@app.route('/cone/<percap>/<shape>', methods=["GET","POST"],endpoint='cone')
def calculatecone(percap,shape):
    if request.method=="POST":
        radius=request.form['r']
        height=request.form['h']
        volume=int(height)*int(radius)*int(radius)*3.14*int(percap)
        if(shape==1):
            return jsonify("Cost of making cylinder trophy  :"+str(int(volume)))
        else:
            return jsonify("Cost of making conical trophy  :"+str(int(volume/3)))
    else:
        return render_template("coneorcylinder.html")

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        if request.form.getlist("operation")[0]=="skip":
            return redirect(url_for("shapes"))
        else:
            return redirect(url_for("addshapes"))
    return '''<form method="post">
        <input type="checkbox" name="operation" value="skip" checked>SKIP
        <input type="checkbox" name="operation" value="add" checked>ADD SHAPES
        <input type="submit">
        </form>'''
@app.route('/addshapes',methods=['GET','POST'])
def addshapes(shapelist=shapeslist):
    if request.method=="POST":
        shape_name=request.form["shape"]
        cost=request.form["cost"]
        idx=len(shapeslist)
        shapelist.append({'name':shape_name, 'id':idx, 'cost':cost})
        return redirect(url_for("shapes"))
    else:
        return render_template("add.html")
if __name__ == '__main__':
    app.run()
