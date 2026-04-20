from functools import reduce  
  
  
def update_profile(user_id, **data):  
    result = {"id": user_id}  
    result["updated_fields"] = dict(data)  
    return result  
  
  
def get_domains(emails):  
    return map(lambda email: email.partition("@")[2], emails)  
  
  
def filter_target_audience(users):  
    return filter(  
        lambda user: user.get("age", 0) >= 18 and user.get("is_premium", False),  
        users,  
    )  
  
  
def build_response(status_code, *errors, **payload):  
    result = {  
        "status": status_code,  
        "errors": tuple(errors),  
        "data": dict(payload),  
    }  
    return result  
  
  
def calculate_total_spent(transactions):  
    return reduce(  
        lambda total, transaction: total + transaction.get("amount", 0),  
        transactions,  
        0,  
    )  
