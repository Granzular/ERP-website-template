''' 
modules contains helper functions for tge sales app'''
import uuid,base64
from customers.models import Customer
from profiles.models import Staff
from io import BytesIO
import matplotlib.pyplot as plt


def generate_code()->str:
    '''generates a unique id using uuid module. id is limited to 12 characters'''
    code = str(uuid.uuid4()).replace('-','')[:12]
    return code

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer.name

def get_salesman_from_id(val):
    salesman = Staff.objects.get(id=val)
    return salesman.user.username

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type,result_by,d,**kwargs):
    plt.style.use('bmh')
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,4))
    key = (lambda x:"transaction_id" if x=="#1" else "created" if x=="#2" else None )(result_by)
    d =(lambda x:d.groupby("created",as_index=False)['total_price'].agg('sum') if x=="created" else d)(key)

    if chart_type == '#1':
        plt.bar(d[key],d['total_price'])
        
    elif chart_type == '#2':

        plt.pie(data=d,x="total_price",labels=key)

    elif chart_type == '#3':
        plt.plot(d[key],d['total_price'])
    else:
        print('invalid chart_type ')
    plt.tight_layout()
    chart = get_graph()
    return chart

