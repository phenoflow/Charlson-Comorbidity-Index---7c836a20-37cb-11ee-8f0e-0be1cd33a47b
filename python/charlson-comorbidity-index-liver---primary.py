# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"A702.00","system":"readv2"},{"code":"A702000","system":"readv2"},{"code":"A703.00","system":"readv2"},{"code":"A703000","system":"readv2"},{"code":"A704000","system":"readv2"},{"code":"A705000","system":"readv2"},{"code":"A705100","system":"readv2"},{"code":"A707.00","system":"readv2"},{"code":"A707000","system":"readv2"},{"code":"A707100","system":"readv2"},{"code":"A707200","system":"readv2"},{"code":"A707X00","system":"readv2"},{"code":"A70z000","system":"readv2"},{"code":"C350012","system":"readv2"},{"code":"J610.00","system":"readv2"},{"code":"J611.00","system":"readv2"},{"code":"J612.00","system":"readv2"},{"code":"J612.11","system":"readv2"},{"code":"J612.12","system":"readv2"},{"code":"J612000","system":"readv2"},{"code":"J613.00","system":"readv2"},{"code":"J613000","system":"readv2"},{"code":"J614.00","system":"readv2"},{"code":"J614000","system":"readv2"},{"code":"J614100","system":"readv2"},{"code":"J614111","system":"readv2"},{"code":"J614200","system":"readv2"},{"code":"J614300","system":"readv2"},{"code":"J614400","system":"readv2"},{"code":"J614y00","system":"readv2"},{"code":"J614z00","system":"readv2"},{"code":"J615.00","system":"readv2"},{"code":"J615.11","system":"readv2"},{"code":"J615100","system":"readv2"},{"code":"J615300","system":"readv2"},{"code":"J615400","system":"readv2"},{"code":"J615500","system":"readv2"},{"code":"J615600","system":"readv2"},{"code":"J615700","system":"readv2"},{"code":"J615800","system":"readv2"},{"code":"J615812","system":"readv2"},{"code":"J615C00","system":"readv2"},{"code":"J615D00","system":"readv2"},{"code":"J615H00","system":"readv2"},{"code":"J615y00","system":"readv2"},{"code":"J615z00","system":"readv2"},{"code":"J615z11","system":"readv2"},{"code":"J615z12","system":"readv2"},{"code":"J615z13","system":"readv2"},{"code":"J615z15","system":"readv2"},{"code":"J616.00","system":"readv2"},{"code":"J616000","system":"readv2"},{"code":"J616100","system":"readv2"},{"code":"J616200","system":"readv2"},{"code":"J616z00","system":"readv2"},{"code":"J617.00","system":"readv2"},{"code":"J617000","system":"readv2"},{"code":"J61y.00","system":"readv2"},{"code":"J61y100","system":"readv2"},{"code":"J61y200","system":"readv2"},{"code":"J61y300","system":"readv2"},{"code":"J61y400","system":"readv2"},{"code":"J61y500","system":"readv2"},{"code":"J61y600","system":"readv2"},{"code":"J61y700","system":"readv2"},{"code":"J61y800","system":"readv2"},{"code":"J61yz00","system":"readv2"},{"code":"J61z.00","system":"readv2"},{"code":"J62..00","system":"readv2"},{"code":"J630.00","system":"readv2"},{"code":"J635300","system":"readv2"},{"code":"J635400","system":"readv2"},{"code":"J635500","system":"readv2"},{"code":"J635600","system":"readv2"},{"code":"J63B.00","system":"readv2"},{"code":"J63X.00","system":"readv2"},{"code":"Jyu7100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["charlson-comorbidity-index-liver---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["charlson-comorbidity-index-liver---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["charlson-comorbidity-index-liver---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
