from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import engine, load_queue_from_db, load_returnDetails_from_db, load_tracking_id_to_search


app = Flask(__name__)






@app.route('/', methods=['POST', 'GET'])
def index(): 
  returnDetails = load_returnDetails_from_db()
  tracking_id = load_tracking_id_to_search()
  queue = load_queue_from_db()
  if (returnDetails and tracking_id):  #if they exist
    tasks = queue
    #TrackingIDS.query.order_by(TrackingIDS.date_created).all()
    return render_template('home.html', tasks=tasks, passed_value = output_data, tracking_id=tracking_id)
        

  else: 
      return render_template('home.html', tasks=queue)
      
@app.route('/refresh_returns_and_inventory')
def refresh():
    try:
        #db.session.delete(task_to_delete)
        #db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem refreshing your returns'

@app.route('/result', methods =['POST', 'GET'])
def result():
    tracking_id = request.form
    #output = request.form.to_dict()
    #tracking_id=output["track"]
    output_data = run_script_getReturns(tracking_id)
    return render_template('home.html', passed_value=output_data, tracking_id=tracking_id)
    #return render_template('result.html', output_data=output_data)

@app.route('/info_for_tracking_id', methods =[ 'POST', 'GET'])
def get_info_on_track():
    #task_to_delete = TrackingIDS.query.get_or_404(id)
    #update the database to include data for the return

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem getting the info for this return'

@app.route('/increase_inventory', methods =['POST', 'GET'])
def increase_inventory():
  #take the tracking id's in the queue and increase inventory by the return order amount for each
   return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = TrackingIDS.query.get_or_404(id)

    try:
        #db.session.delete(task_to_delete)
        #db.session.commit()
      
        return redirect('/')
    except:
        return 'There was a problem deleting that task'




"""  
     
def inventoryCheck():
    run_script_checkInventoryIncrease(passed_valuefromHTML[Quantity_of_SKU], passed_valuefromHTML[return_quantity]):
    


    return render_template('Amazon.html', passed_value_inventoryCheck = output_data)
   """

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)