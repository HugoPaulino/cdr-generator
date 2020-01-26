import random
from .constants import number_list, max_numbers_to_generate, perfix_list, max_n_perfixes,max_n_sms,max_call_duration,max_n_seconds 
import pandas as pd 
import numpy as np

def generate_msisdn_list(number_samples):
    """

    """
    print("Start generating {} msisdns".format(number_samples))
    msisdn_list = [ ]
    for i in range(1,number_samples):
        msisdns_list = random.sample(number_list, max_numbers_to_generate) # generate 5 random numbers from 1 to 9 to a list
        
        msisdn = list_to_string(msisdns_list)

        number_perfix  = perfix_list[random.randrange(max_n_perfixes)]

        msisdn = number_perfix+msisdn # append prefix more random number
        msisdn_list.append(msisdn)
    
    return msisdn_list



def generate_sms(number_samples):
    """
    
    """
    sms_list = [ ]
    for i in range(1,number_samples):
        max_numbers = random.randrange(1,max_n_sms)
        sms_list.append(max_numbers)
    return sms_list

def generate_call_duration(number_samples):
    """
    
    """
    call_duration_list = [ ]
    for i in range(1,number_samples):
        call_duration_min = random.randrange(1,max_call_duration)
        call_duration_sec = random.randrange(1,max_n_seconds)
        call_duration = float(str(call_duration_min)+ "."+str(call_duration_sec))
        call_duration_list.append(call_duration)
    return call_duration_list


def generate_datetimes(number_samples):
    date_times = []
    times = pd.date_range('2020-01-01', periods=289, freq='5min')
    date_times = np.array(times)

    
    return date_times[:9]

def create_dataframe(date_times,msisdn_origin,msisdn_dest,call_duration,n_sms):
    df = pd.DataFrame(
    {'timestamp': date_times,
     'msisdn_origin': msisdn_origin,
     'msisdn_dest': msisdn_dest,
     'call_duration': call_duration,
     'sms_number': n_sms
    })
    return df


def write_csv_data(dataframe):
    dataframe.to_csv ("data.csv", index = None, header=True)

def list_to_string(number_list):  
    """
    
    """
    number_string = "" 
    number_list = map(str, number_list)
    return number_string.join(number_list)


def order_list_random(msisdn_list):
    """
    
    """
    list_aux = list(msisdn_list)
    random.shuffle(list_aux)
    return list_aux

if __name__ == "__main__":
    print ("test")