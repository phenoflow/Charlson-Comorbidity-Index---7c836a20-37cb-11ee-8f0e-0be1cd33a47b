# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"E00..00","system":"readv2"},{"code":"E00..11","system":"readv2"},{"code":"E00..12","system":"readv2"},{"code":"E000.00","system":"readv2"},{"code":"E001.00","system":"readv2"},{"code":"E001000","system":"readv2"},{"code":"E001100","system":"readv2"},{"code":"E001200","system":"readv2"},{"code":"E001300","system":"readv2"},{"code":"E001z00","system":"readv2"},{"code":"E002.00","system":"readv2"},{"code":"E002000","system":"readv2"},{"code":"E002100","system":"readv2"},{"code":"E002z00","system":"readv2"},{"code":"E003.00","system":"readv2"},{"code":"E004.00","system":"readv2"},{"code":"E004.11","system":"readv2"},{"code":"E004000","system":"readv2"},{"code":"E004100","system":"readv2"},{"code":"E004200","system":"readv2"},{"code":"E004300","system":"readv2"},{"code":"E004z00","system":"readv2"},{"code":"Eu00.00","system":"readv2"},{"code":"Eu00000","system":"readv2"},{"code":"Eu00011","system":"readv2"},{"code":"Eu00012","system":"readv2"},{"code":"Eu00013","system":"readv2"},{"code":"Eu00100","system":"readv2"},{"code":"Eu00111","system":"readv2"},{"code":"Eu00112","system":"readv2"},{"code":"Eu00113","system":"readv2"},{"code":"Eu00200","system":"readv2"},{"code":"Eu00z00","system":"readv2"},{"code":"Eu00z11","system":"readv2"},{"code":"Eu01.00","system":"readv2"},{"code":"Eu01.11","system":"readv2"},{"code":"Eu01000","system":"readv2"},{"code":"Eu01100","system":"readv2"},{"code":"Eu01111","system":"readv2"},{"code":"Eu01200","system":"readv2"},{"code":"Eu01300","system":"readv2"},{"code":"Eu01y00","system":"readv2"},{"code":"Eu01z00","system":"readv2"},{"code":"Eu02.00","system":"readv2"},{"code":"Eu02000","system":"readv2"},{"code":"Eu02100","system":"readv2"},{"code":"Eu02200","system":"readv2"},{"code":"Eu02300","system":"readv2"},{"code":"Eu02400","system":"readv2"},{"code":"Eu02500","system":"readv2"},{"code":"Eu02y00","system":"readv2"},{"code":"Eu02z00","system":"readv2"},{"code":"Eu02z11","system":"readv2"},{"code":"Eu02z13","system":"readv2"},{"code":"Eu02z14","system":"readv2"},{"code":"Eu02z16","system":"readv2"},{"code":"Eu04100","system":"readv2"},{"code":"F110000","system":"readv2"},{"code":"F110100","system":"readv2"},{"code":"F111.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["charlson-comorbidity-index-dementium---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["charlson-comorbidity-index-dementium---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["charlson-comorbidity-index-dementium---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
