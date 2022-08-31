import os, glob

if __name__ == '__main__':
    txt_list = glob.glob("F:/AI资料/ObjdetectBoatsCars/dataset/CarsDatasetGreyScaled/labels/test/*.txt")
    for txt_item in txt_list:
        with open(txt_item) as f:
            liens = f.readlines()
        with open(txt_item, 'w') as f:
            for line in liens:
                line_split = line.strip().split()
                line_split[0]='2'
                f.write(
                    line_split[0]+' '+
                    line_split[1]+" "+
                    line_split[2]+" "+
                    line_split[3]+" "+
                    line_split[4]+'\n'
                )