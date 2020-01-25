from .helpers import *

class CDR_Generator:
    
    @staticmethod
    def run(args):
        
        number_of_samples = args[1]
        number_of_samples = int(number_of_samples)
        datetimes = generate_datetimes(int(number_of_samples))
        msisdn_origin_list = generate_msisdn_list(int(number_of_samples))
        msisdn_dest_list =  order_list_random(msisdn_origin_list)

        call_duration = generate_call_duration(number_of_samples)
        sms_list = generate_sms(number_of_samples)

        df = create_dataframe(datetimes,msisdn_origin_list,msisdn_dest_list,call_duration,sms_list )
        write_csv_data(df)
        print(datetimes)
        print("msisdn_origin_list",msisdn_origin_list)
        print("msisdn_dest_list ",msisdn_dest_list)
        print("call_duration",call_duration)
        print("sms_list",sms_list)

        



#if __name__ == "__main__":
#    print ("test")