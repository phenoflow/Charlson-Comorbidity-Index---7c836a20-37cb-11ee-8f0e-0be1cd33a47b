# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"14A6.00","system":"readv2"},{"code":"14B3.00","system":"readv2"},{"code":"14B3.11","system":"readv2"},{"code":"14B4.00","system":"readv2"},{"code":"173A.00","system":"readv2"},{"code":"173c.00","system":"readv2"},{"code":"1O1..00","system":"readv2"},{"code":"1O2..00","system":"readv2"},{"code":"663..00","system":"readv2"},{"code":"663..11","system":"readv2"},{"code":"663..12","system":"readv2"},{"code":"663J.00","system":"readv2"},{"code":"663K.00","system":"readv2"},{"code":"663N.00","system":"readv2"},{"code":"663N000","system":"readv2"},{"code":"663N100","system":"readv2"},{"code":"663N200","system":"readv2"},{"code":"663O.00","system":"readv2"},{"code":"663O000","system":"readv2"},{"code":"663P.00","system":"readv2"},{"code":"663Q.00","system":"readv2"},{"code":"663U.00","system":"readv2"},{"code":"663V.00","system":"readv2"},{"code":"663V000","system":"readv2"},{"code":"663V100","system":"readv2"},{"code":"663V200","system":"readv2"},{"code":"663V300","system":"readv2"},{"code":"663W.00","system":"readv2"},{"code":"663d.00","system":"readv2"},{"code":"663e.00","system":"readv2"},{"code":"663e100","system":"readv2"},{"code":"663f.00","system":"readv2"},{"code":"663h.00","system":"readv2"},{"code":"663j.00","system":"readv2"},{"code":"663m.00","system":"readv2"},{"code":"663n.00","system":"readv2"},{"code":"663p.00","system":"readv2"},{"code":"663q.00","system":"readv2"},{"code":"663r.00","system":"readv2"},{"code":"663s.00","system":"readv2"},{"code":"663t.00","system":"readv2"},{"code":"663u.00","system":"readv2"},{"code":"663v.00","system":"readv2"},{"code":"663w.00","system":"readv2"},{"code":"663x.00","system":"readv2"},{"code":"663y.00","system":"readv2"},{"code":"66Y5.00","system":"readv2"},{"code":"66Y9.00","system":"readv2"},{"code":"66YA.00","system":"readv2"},{"code":"66YB.00","system":"readv2"},{"code":"66YC.00","system":"readv2"},{"code":"66YD.00","system":"readv2"},{"code":"66YE.00","system":"readv2"},{"code":"66YI.00","system":"readv2"},{"code":"66YJ.00","system":"readv2"},{"code":"66YK.00","system":"readv2"},{"code":"66YL.00","system":"readv2"},{"code":"66YL.11","system":"readv2"},{"code":"66YL.12","system":"readv2"},{"code":"66YM.00","system":"readv2"},{"code":"66YP.00","system":"readv2"},{"code":"66YQ.00","system":"readv2"},{"code":"66YR.00","system":"readv2"},{"code":"66YS.00","system":"readv2"},{"code":"66YT.00","system":"readv2"},{"code":"66YZ.00","system":"readv2"},{"code":"66Yd.00","system":"readv2"},{"code":"66Ye.00","system":"readv2"},{"code":"66Yf.00","system":"readv2"},{"code":"66Yg.00","system":"readv2"},{"code":"66Yh.00","system":"readv2"},{"code":"66Yi.00","system":"readv2"},{"code":"66Yj.00","system":"readv2"},{"code":"66Yk.00","system":"readv2"},{"code":"66Yl.00","system":"readv2"},{"code":"8H2P.00","system":"readv2"},{"code":"8H2R.00","system":"readv2"},{"code":"9OJ..00","system":"readv2"},{"code":"9OJ..11","system":"readv2"},{"code":"9OJ1.00","system":"readv2"},{"code":"9OJ2.00","system":"readv2"},{"code":"9OJ3.00","system":"readv2"},{"code":"9OJ4.00","system":"readv2"},{"code":"9OJ5.00","system":"readv2"},{"code":"9OJ6.00","system":"readv2"},{"code":"9OJ7.00","system":"readv2"},{"code":"9OJ8.00","system":"readv2"},{"code":"9OJ9.00","system":"readv2"},{"code":"9OJA.00","system":"readv2"},{"code":"9OJA.11","system":"readv2"},{"code":"9OJZ.00","system":"readv2"},{"code":"G400.00","system":"readv2"},{"code":"G41z.11","system":"readv2"},{"code":"G581.11","system":"readv2"},{"code":"H3...00","system":"readv2"},{"code":"H3...11","system":"readv2"},{"code":"H31..00","system":"readv2"},{"code":"H310.00","system":"readv2"},{"code":"H310000","system":"readv2"},{"code":"H310100","system":"readv2"},{"code":"H310z00","system":"readv2"},{"code":"H311.00","system":"readv2"},{"code":"H311000","system":"readv2"},{"code":"H311100","system":"readv2"},{"code":"H311z00","system":"readv2"},{"code":"H312.00","system":"readv2"},{"code":"H312000","system":"readv2"},{"code":"H312011","system":"readv2"},{"code":"H312100","system":"readv2"},{"code":"H312200","system":"readv2"},{"code":"H312300","system":"readv2"},{"code":"H312z00","system":"readv2"},{"code":"H313.00","system":"readv2"},{"code":"H31y.00","system":"readv2"},{"code":"H31y000","system":"readv2"},{"code":"H31y100","system":"readv2"},{"code":"H31yz00","system":"readv2"},{"code":"H31z.00","system":"readv2"},{"code":"H32..00","system":"readv2"},{"code":"H320.00","system":"readv2"},{"code":"H320000","system":"readv2"},{"code":"H320100","system":"readv2"},{"code":"H320200","system":"readv2"},{"code":"H320300","system":"readv2"},{"code":"H320z00","system":"readv2"},{"code":"H321.00","system":"readv2"},{"code":"H322.00","system":"readv2"},{"code":"H32y.00","system":"readv2"},{"code":"H32y000","system":"readv2"},{"code":"H32y100","system":"readv2"},{"code":"H32y111","system":"readv2"},{"code":"H32y200","system":"readv2"},{"code":"H32yz00","system":"readv2"},{"code":"H32z.00","system":"readv2"},{"code":"H33..00","system":"readv2"},{"code":"H33..11","system":"readv2"},{"code":"H330.00","system":"readv2"},{"code":"H330.11","system":"readv2"},{"code":"H330.12","system":"readv2"},{"code":"H330.13","system":"readv2"},{"code":"H330.14","system":"readv2"},{"code":"H330000","system":"readv2"},{"code":"H330011","system":"readv2"},{"code":"H330100","system":"readv2"},{"code":"H330111","system":"readv2"},{"code":"H330z00","system":"readv2"},{"code":"H331.00","system":"readv2"},{"code":"H331.11","system":"readv2"},{"code":"H331000","system":"readv2"},{"code":"H331100","system":"readv2"},{"code":"H331111","system":"readv2"},{"code":"H331z00","system":"readv2"},{"code":"H332.00","system":"readv2"},{"code":"H333.00","system":"readv2"},{"code":"H334.00","system":"readv2"},{"code":"H33z.00","system":"readv2"},{"code":"H33z.11","system":"readv2"},{"code":"H33z000","system":"readv2"},{"code":"H33z011","system":"readv2"},{"code":"H33z100","system":"readv2"},{"code":"H33z111","system":"readv2"},{"code":"H33z200","system":"readv2"},{"code":"H33zz00","system":"readv2"},{"code":"H33zz11","system":"readv2"},{"code":"H33zz12","system":"readv2"},{"code":"H33zz13","system":"readv2"},{"code":"H34..00","system":"readv2"},{"code":"H340.00","system":"readv2"},{"code":"H341.00","system":"readv2"},{"code":"H34z.00","system":"readv2"},{"code":"H35..00","system":"readv2"},{"code":"H350.00","system":"readv2"},{"code":"H351.00","system":"readv2"},{"code":"H352.00","system":"readv2"},{"code":"H352000","system":"readv2"},{"code":"H352100","system":"readv2"},{"code":"H352z00","system":"readv2"},{"code":"H353.00","system":"readv2"},{"code":"H354.00","system":"readv2"},{"code":"H355.00","system":"readv2"},{"code":"H356.00","system":"readv2"},{"code":"H357.00","system":"readv2"},{"code":"H35y.00","system":"readv2"},{"code":"H35y000","system":"readv2"},{"code":"H35y100","system":"readv2"},{"code":"H35y200","system":"readv2"},{"code":"H35y500","system":"readv2"},{"code":"H35y600","system":"readv2"},{"code":"H35y700","system":"readv2"},{"code":"H35y800","system":"readv2"},{"code":"H35yz00","system":"readv2"},{"code":"H35z.00","system":"readv2"},{"code":"H35z000","system":"readv2"},{"code":"H35z100","system":"readv2"},{"code":"H35zz00","system":"readv2"},{"code":"H36..00","system":"readv2"},{"code":"H37..00","system":"readv2"},{"code":"H38..00","system":"readv2"},{"code":"H39..00","system":"readv2"},{"code":"H3y..00","system":"readv2"},{"code":"H3y..11","system":"readv2"},{"code":"H3y0.00","system":"readv2"},{"code":"H3y1.00","system":"readv2"},{"code":"H3z..00","system":"readv2"},{"code":"H3z..11","system":"readv2"},{"code":"H4...00","system":"readv2"},{"code":"H4...11","system":"readv2"},{"code":"H4...12","system":"readv2"},{"code":"H40..00","system":"readv2"},{"code":"H41..00","system":"readv2"},{"code":"H410.00","system":"readv2"},{"code":"H410.11","system":"readv2"},{"code":"H41z.00","system":"readv2"},{"code":"H42..00","system":"readv2"},{"code":"H420.00","system":"readv2"},{"code":"H421.00","system":"readv2"},{"code":"H422.00","system":"readv2"},{"code":"H423.00","system":"readv2"},{"code":"H42z.00","system":"readv2"},{"code":"H43..00","system":"readv2"},{"code":"H431.00","system":"readv2"},{"code":"H432.00","system":"readv2"},{"code":"H433.00","system":"readv2"},{"code":"H434.00","system":"readv2"},{"code":"H435.00","system":"readv2"},{"code":"H43z.00","system":"readv2"},{"code":"H44..00","system":"readv2"},{"code":"H440.00","system":"readv2"},{"code":"H441.00","system":"readv2"},{"code":"H44z.00","system":"readv2"},{"code":"H45..00","system":"readv2"},{"code":"H450.00","system":"readv2"},{"code":"H46..00","system":"readv2"},{"code":"H460.00","system":"readv2"},{"code":"H460z00","system":"readv2"},{"code":"H462.00","system":"readv2"},{"code":"H463.00","system":"readv2"},{"code":"H464.00","system":"readv2"},{"code":"H464000","system":"readv2"},{"code":"H464100","system":"readv2"},{"code":"H464200","system":"readv2"},{"code":"H464z00","system":"readv2"},{"code":"H46z.00","system":"readv2"},{"code":"H46zz00","system":"readv2"},{"code":"H48..00","system":"readv2"},{"code":"H4y..00","system":"readv2"},{"code":"H4y1.00","system":"readv2"},{"code":"H4y1000","system":"readv2"},{"code":"H4y1z00","system":"readv2"},{"code":"H4y2.00","system":"readv2"},{"code":"H4y2100","system":"readv2"},{"code":"H4yy.00","system":"readv2"},{"code":"H4yz.00","system":"readv2"},{"code":"H4z..00","system":"readv2"},{"code":"H541000","system":"readv2"},{"code":"H55..00","system":"readv2"},{"code":"H55..11","system":"readv2"},{"code":"H563.00","system":"readv2"},{"code":"H563.11","system":"readv2"},{"code":"H563.12","system":"readv2"},{"code":"H563100","system":"readv2"},{"code":"H563z00","system":"readv2"},{"code":"H564.00","system":"readv2"},{"code":"H570.00","system":"readv2"},{"code":"H57y000","system":"readv2"},{"code":"H57y100","system":"readv2"},{"code":"H57y200","system":"readv2"},{"code":"H57y300","system":"readv2"},{"code":"H57y400","system":"readv2"},{"code":"H581.00","system":"readv2"},{"code":"H582.00","system":"readv2"},{"code":"H58y300","system":"readv2"},{"code":"Hyu3.00","system":"readv2"},{"code":"Hyu3000","system":"readv2"},{"code":"Hyu3100","system":"readv2"},{"code":"Hyu4200","system":"readv2"},{"code":"Hyu4700","system":"readv2"},{"code":"Hyu4900","system":"readv2"},{"code":"Hyu5.00","system":"readv2"},{"code":"Hyu5000","system":"readv2"},{"code":"Hyu5100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pulmonary-charlson-comorbidity-index---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pulmonary-charlson-comorbidity-index---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pulmonary-charlson-comorbidity-index---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)