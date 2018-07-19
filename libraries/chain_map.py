from collections import ChainMap
# class used to create multiple mappings into single mapping
quote_data = {'age': 23,
              'gender': 'F',
              'sum_assured': 10000000,
              'salary': 500000,
              'maturity_age': 60,
              'tobacco_user': 'N'}

base_premium_data = {'base_premium': 644,
                     'premium_frequency': 'M',
                     'total_premium': 700,
                     }

rider_premium_data = {
    'accidental_death_premium': 50,
    'wop_premium': 6,
}

plan_data = {
    'insurer': 'kotak',
    'slug': 'e-term',
}

plan_list = ChainMap(plan_data, base_premium_data, rider_premium_data, quote_data)
print("you have to pay Rs.%s to %s for buying plan %s"%(plan_list['total_premium'], plan_list['insurer'], plan_list['slug']))
