# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"283..00","system":"readv2"},{"code":"2832.11","system":"readv2"},{"code":"2833.00","system":"readv2"},{"code":"2834.00","system":"readv2"},{"code":"2835.00","system":"readv2"},{"code":"2836.00","system":"readv2"},{"code":"2837.00","system":"readv2"},{"code":"283Z.00","system":"readv2"},{"code":"F141.00","system":"readv2"},{"code":"F22..00","system":"readv2"},{"code":"F22..11","system":"readv2"},{"code":"F220.00","system":"readv2"},{"code":"F221.00","system":"readv2"},{"code":"F222.00","system":"readv2"},{"code":"F222.11","system":"readv2"},{"code":"F223.00","system":"readv2"},{"code":"F223.11","system":"readv2"},{"code":"F22z.00","system":"readv2"},{"code":"F230.11","system":"readv2"},{"code":"F230000","system":"readv2"},{"code":"F230100","system":"readv2"},{"code":"F230z00","system":"readv2"},{"code":"F231.00","system":"readv2"},{"code":"F232.00","system":"readv2"},{"code":"F232.11","system":"readv2"},{"code":"F234.00","system":"readv2"},{"code":"F24..00","system":"readv2"},{"code":"F240.00","system":"readv2"},{"code":"F240.11","system":"readv2"},{"code":"F240000","system":"readv2"},{"code":"F240100","system":"readv2"},{"code":"F241.00","system":"readv2"},{"code":"F241000","system":"readv2"},{"code":"F241100","system":"readv2"},{"code":"F242.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["charlson-comorbidity-index-hemiplegia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["charlson-comorbidity-index-hemiplegia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["charlson-comorbidity-index-hemiplegia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
