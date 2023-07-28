import pandas as pd


query = pd.read_csv("overclaws.csv")

for i in range(len(query)):
        print(f'curl -v "http://10.0.44.22:8080/av_integration_momo_vcl/reverseTransaction?msisdn={query.loc[i, "msisdn"]}&externalRef={query.loc[i, "transactionid"]}&amount={query.loc[i, "amount"]}"')