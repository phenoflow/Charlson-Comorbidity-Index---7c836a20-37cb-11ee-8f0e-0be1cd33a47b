# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"14AM.00","system":"readv2"},{"code":"662T.00","system":"readv2"},{"code":"662g.00","system":"readv2"},{"code":"662h.00","system":"readv2"},{"code":"662i.00","system":"readv2"},{"code":"8B29.00","system":"readv2"},{"code":"8CL3.00","system":"readv2"},{"code":"G210100","system":"readv2"},{"code":"G211100","system":"readv2"},{"code":"G21z100","system":"readv2"},{"code":"G232.00","system":"readv2"},{"code":"G234.00","system":"readv2"},{"code":"G58..00","system":"readv2"},{"code":"G58..11","system":"readv2"},{"code":"G580.00","system":"readv2"},{"code":"G580.11","system":"readv2"},{"code":"G580.12","system":"readv2"},{"code":"G580.13","system":"readv2"},{"code":"G580.14","system":"readv2"},{"code":"G580000","system":"readv2"},{"code":"G580100","system":"readv2"},{"code":"G580200","system":"readv2"},{"code":"G580300","system":"readv2"},{"code":"G580400","system":"readv2"},{"code":"G581.00","system":"readv2"},{"code":"G581.13","system":"readv2"},{"code":"G581000","system":"readv2"},{"code":"G582.00","system":"readv2"},{"code":"G58z.00","system":"readv2"},{"code":"G58z.11","system":"readv2"},{"code":"G58z.12","system":"readv2"},{"code":"G5y4z00","system":"readv2"},{"code":"SP11100","system":"readv2"},{"code":"SP11111","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["charlson-comorbidity-index-cardiac---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["charlson-comorbidity-index-cardiac---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["charlson-comorbidity-index-cardiac---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
