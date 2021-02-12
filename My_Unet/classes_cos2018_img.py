
class RGBClassesCodes:

    def __init__(self):
        rgb_codes = [(230,0,77),(230,0,20),(255,0,0),(255,0,50),(255,0,80),(255,0,110),(204,77,242),(204,77,210),(204,77,160),(204,77,120),(204,77,90),(204,77,70),(204,77,40),(204,0,0),(154,0,0),(230,204,204),(230,180,204),(230,150,204),(230,204,230),(210,204,230),(166,0,204),(110,0,204),(166,77,0),(166,16,0),(255,77,255),(255,230,255),(255,210,255),(255,140,255),(230,100,255),(190,100,255),(160,100,255),(255,166,255),(255,255,0),(230,230,0),(230,128,0),(242,166,77),(230,166,0),(255,230,166),(255,240,166),(250,250,166),(255,230,77),(230,204,77),(230,204,130),(255,255,77),(204,242,77),(242,204,166),(220,204,166),(200,204,166),(180,204,166),(160,215,166),(160,230,166),(160,255,166),(128,255,0),(128,235,0),(128,215,0),(128,200,0),(128,180,0),(128,160,0),(128,140,0),(0,166,0),(0,140,0),(0,120,0),(166,255,128),(166,255,128),(230,230,230),(230,230,215),(204,204,204),(166,166,255),(204,204,255),(166,166,230),(0,204,242),(0,242,242),(128,242,230),(128,222,230),(128,200,230),(128,180,230),(128,160,230),(230,230,255),(230,255,255),(0,255,166),(166,255,230),(230,242,255)]
        cos2018_classes = ['1.1.1.1', '1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.3.1', '1.1.3.2', '1.2.1.1', '1.2.2.1', '1.2.3.1', '1.3.1.1', '1.3.1.2', '1.3.2.1', '1.3.2.2', '1.4.1.1', '1.4.1.2','1.4.2.1','1.4.2.2','1.4.2.3','1.4.3.1','1.4.3.2','1.5.1.1','1.5.1.2','1.5.2.1','1.5.2.2','1.5.3.1','1.6.1.1','1.6.1.2','1.6.2.2','1.6.3.1','1.6.4.1','1.6.5.1','1.7.1.1','2.1.1.1','2.1.1.2','2.2.1.1','2.2.2.1','2.2.3.1','2.3.1.1','2.3.1.2','2.3.1.3','2.3.2.1','2.3.3.1','2.4.1.1','3.1.1.1','3.1.2.1','4.1.1.1','4.1.1.2','4.1.1.3','4.1.1.4','4.1.1.5','4.1.1.6','4.1.1.7','5.1.1.1','5.1.1.2','5.1.1.3','5.1.1.4','5.1.1.5','5.1.1.6','5.1.1.7','5.1.2.1','5.1.2.2','5.1.2.3','6.1.1.1','7.1.1.1','7.1.1.2','7.1.2.1','7.1.3.1','8.1.1.1','8.1.2.1','8.1.2.2','9.1.1.1','9.1.1.2','9.1.2.1','9.1.2.2','9.1.2.3','9.1.2.4','9.1.2.5','9.2.1.1','9.3.1.1','9.3.2.1','9.3.3.1','9.3.4.1']

        #rgb_dict = dict(zip(cos2018_classes,rgb_codes))
        self.cos2018_rgb_dict = {
                    '1.1.1.1':	(230,0,77),
                    '1.1.1.2':	(230,0,20),
                    '1.1.2.1':	(255,0,0),
                    '1.1.2.2':	(255,0,50),
                    '1.1.3.1':	(255,0,80),
                    '1.1.3.2':	(255,0,110),
                    '1.2.1.1':	(204,77,242),
                    '1.2.2.1':	(204,77,210),
                    '1.2.3.1':	(204,77,160),
                    '1.3.1.1':	(204,77,120),
                    '1.3.1.2':	(204,77,90),
                    '1.3.2.1':	(204,77,70),
                    '1.3.2.2':	(204,77,40),
                    '1.4.1.1':	(204,0,0),
                    '1.4.1.2':	(154,0,0),
                    '1.4.2.1':	(230,204,204),
                    '1.4.2.2':	(230,180,204),
                    '1.4.2.3':	(230,150,204),
                    '1.4.3.1':	(230,204,230),
                    '1.4.3.2':	(210,204,230),
                    '1.5.1.1':	(166,0,204),
                    '1.5.1.2':	(110,0,204),
                    '1.5.2.1':	(166,77,0),
                    '1.5.2.2':	(166,16,0),
                    '1.5.3.1':	(255,77,255),
                    '1.6.1.1':	(255,230,255),
                    '1.6.1.2':	(255,210,255),
                    '1.6.2.2':	(255,140,255),
                    '1.6.3.1':	(230,100,255),
                    '1.6.4.1':	(190,100,255),
                    '1.6.5.1':	(160,100,255),
                    '1.7.1.1':	(255,166,255),
                    '2.1.1.1':	(255,255,0),
                    '2.1.1.2':	(230,230,0),
                    '2.2.1.1':	(230,128,0),
                    '2.2.2.1':	(242,166,77),
                    '2.2.3.1':	(230,166,0),
                    '2.3.1.1':	(255,230,166),
                    '2.3.1.2':	(255,240,166),
                    '2.3.1.3':	(250,250,166),
                    '2.3.2.1':	(255,230,77),
                    '2.3.3.1':	(230,204,77),
                    '2.4.1.1':	(230,204,130),
                    '3.1.1.1':	(255,255,77),
                    '3.1.2.1':	(204,242,77),
                    '4.1.1.1':	(242,204,166),
                    '4.1.1.2':	(220,204,166),
                    '4.1.1.3':	(200,204,166),
                    '4.1.1.4':	(180,204,166),
                    '4.1.1.5':	(160,215,166),
                    '4.1.1.6':	(160,230,166),
                    '4.1.1.7':	(160,255,166),
                    '5.1.1.1':	(128,255,0),
                    '5.1.1.2':	(128,235,0),
                    '5.1.1.3':	(128,215,0),
                    '5.1.1.4':	(128,200,0),
                    '5.1.1.5':	(128,180,0),
                    '5.1.1.6':	(128,160,0),
                    '5.1.1.7':	(128,140,0),
                    '5.1.2.1':	(0,166,0),
                    '5.1.2.2':	(0,140,0),
                    '5.1.2.3':	(0,120,0),
                    '6.1.1.1':	(166,255,128),
                    '7.1.1.1':	(166,255,128),
                    '7.1.1.2':	(230,230,230),
                    '7.1.2.1':	(230,230,215),
                    '7.1.3.1':	(204,204,204),
                    '8.1.1.1':	(166,166,255),
                    '8.1.2.1':	(204,204,255),
                    '8.1.2.2':	(166,166,230),
                    '9.1.1.1':	(0,204,242),
                    '9.1.1.2':	(0,242,242),
                    '9.1.2.1':	(128,242,230),
                    '9.1.2.2':	(128,222,230),
                    '9.1.2.3':	(128,200,230),
                    '9.1.2.4':	(128,180,230),
                    '9.1.2.5':	(128,160,230),
                    '9.2.1.1':	(230,230,255),
                    '9.3.1.1':	(230,255,255),
                    '9.3.2.1':	(0,255,166),
                    '9.3.3.1':	(166,255,230),
                    '9.3.4.1':	(230,242,255)
        }

        self.rgb_classecode_dict = {
                    '(230,0,77)':	    0,
                    '(230,0,20)':	    1,
                    '(255,0,0)':	    2,
                    '(255,0,50)':	    3,
                    '(255,0,80)':	    4,
                    '(255,0,110)':	    5,
                    '(204,77,242)':	    6,
                    '(204,77,210)':	    7,
                    '(204,77,160)':	    8,
                    '(204,77,120)':	    9,
                    '(204,77,90)':	    10,
                    '(204,77,70)':	    11,
                    '(204,77,40)':	    12,
                    '(204,0,0)':	    13,
                    '(154,0,0)':	    14,
                    '(230,204,204)':	15,
                    '(230,180,204)':	16,
                    '(230,150,204)':	17,
                    '(230,204,230)':	18,
                    '(210,204,230)':	19,
                    '(166,0,204)':	    20,
                    '(110,0,204)':	    21,
                    '(166,77,0)':	    22,
                    '(166,16,0)':	    23,
                    '(255,77,255)':	    24,
                    '(255,230,255)':	25,
                    '(255,210,255)':	26,
                    '(255,140,255)':	27,
                    '(230,100,255)':	28,
                    '(190,100,255)':	29,
                    '(160,100,255)':	30,
                    '(255,166,255)':	31,
                    '(255,255,0)':	    32,
                    '(230,230,0)':	    33,
                    '(230,128,0)':	    34,
                    '(242,166,77)':	    35,
                    '(230,166,0)':	    36,
                    '(255,230,166)':	37,
                    '(255,240,166)':	38,
                    '(250,250,166)':	39,
                    '(255,230,77)':	    40,
                    '(230,204,77)':	    41,
                    '(230,204,130)':	42,
                    '(255,255,77)':	    43,
                    '(204,242,77)':	    44,
                    '(242,204,166)':	45,
                    '(220,204,166)':	46,
                    '(200,204,166)':	47,
                    '(180,204,166)':	48,
                    '(160,215,166)':	49,
                    '(160,230,166)':	50,
                    '(160,255,166)':	51,
                    '(128,255,0)':	    52,
                    '(128,235,0)':	    53,
                    '(128,215,0)':	    54,
                    '(128,200,0)':	    55,
                    '(128,180,0)':	    56,
                    '(128,160,0)':	    57,
                    '(128,140,0)':	    58,
                    '(0,166,0)':	    58,
                    '(0,140,0)':	    59,
                    '(0,120,0)':	    60,
                    '(166,255,128)':	61,
                    '(166,255,128)':	62,
                    '(230,230,230)':	63,
                    '(230,230,215)':	64,
                    '(204,204,204)':	65,
                    '(166,166,255)':	66,
                    '(204,204,255)':	67,
                    '(166,166,230)':	68,
                    '(0,204,242)':	    69,
                    '(0,242,242)':	    70,
                    '(128,242,230)':	71,
                    '(128,222,230)':	72,
                    '(128,200,230)':	73,
                    '(128,180,230)':	74,
                    '(128,160,230)':	75,
                    '(230,230,255)':	76,
                    '(230,255,255)':	77,
                    '(0,255,166)':	    78,
                    '(166,255,230)':	79,
                    '(230,242,255)':	80
        }
        self.rgb_highercode_dict = {
                    (56, 168, 0):   1,
                    (111, 196, 0):  2,
                    (176, 224, 0):  3,
                    (255, 255, 0):  4,
                    (255, 170, 0):  5,
                    (255, 85, 0):   6,
                    (255, 0, 0):    7
        }

    def GetRgbCodes(self, list_codes=None):
        
        out_rgb_list = []
        if list_codes == None:
            out_rgb_list = self.cos2018_rgb_dict.values()
        else:
            list_codes = self.RemakeList(list_codes)
            for cos_classe in list_codes:
                for key in self.cos2018_rgb_dict.keys():
                    if key == cos_classe:
                        out_rgb_list.append(self.cos2018_rgb_dict[key])
                        break

        return out_rgb_list
    
    def RemakeList(self,list_codes):
        out_list=[]
        for cos_classe in list_codes:
            for key in self.cos2018_rgb_dict.keys():
                    
                if len(cos_classe) == 1:
                    if key[0] == cos_classe:
                        out_list.append(key)
                if len(cos_classe) == 3:
                    if key[0:2] == cos_classe:
                        out_list.append(key)
                if len(cos_classe) == 5:
                    if key[:5] == cos_classe:
                        out_list.append(key)
                if len(cos_classe) == 7:
                    if key == cos_classe:
                        out_list.append(key)
                    
        return out_list

    def BuildDynamicDict(self,list_codes):

        new_dict = {}
        pixel_value = 1
        i = 0

        for element in list_codes:

            for code in element:

                for code2018 in self.cos2018_rgb_dict.keys():
                    if str(code2018).startswith(str(code)):
                        new_dict.update({code2018:pixel_value})
                
            pixel_value +=1

        new_dict = self.CosClassRGBSubstituition(new_dict)
        return new_dict

    def CosClassRGBSubstituition(self, cos_dict):
        out_dict={}
        for (code_key, pixel_value) in cos_dict.items():
            if code_key in self.cos2018_rgb_dict.keys():
                out_dict.update({self.cos2018_rgb_dict[code_key]:pixel_value})
            else:
                pass

        return out_dict

# JUST FOR TEST THIS CLASS
# if __name__ == "__main__":
#     classes = RGBClassesCodes()
#     rgb_list = classes.BuildDynamicDict([ '1.1.1.1', ('2.1', '2.2'), '4', '7.1.1'])

    
