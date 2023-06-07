import csv
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from functions import image_show
import pandas as pd 
from data_func import make_new_data,update,save_and_push
import os
from huggingface_hub import Repository
import reader

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)



def pull_read(DATASET_REPO_URL,HF_TOKEN,DATA_FILE):
    
    repo = Repository(
        local_dir="data", clone_from=DATASET_REPO_URL, use_auth_token=HF_TOKEN
        )
    
    with open(DATA_FILE) as csvfile:
        df = pd.read_csv(csvfile) 
        df = pd.DataFrame(df)
    
    return repo, df

@st.cache
def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')  


def screen_scan_main():
    teacher_code = st.text_input("Ogretmen kodu:",key=12)
    password = st.text_input("Sıfre:",key=17,type="password")
    
    teacher_code = str(teacher_code)
    password = str(password)
    
    DATA_FILENAME = f"{teacher_code}.csv"
    DATA_FILENAME = str(DATA_FILENAME)
    
    image_file = st.file_uploader(
        "Tarama Yapmak Icin Optigi Yukleyin", type=['jpeg', 'png', 'jpg', 'webp'])
    if image_file != None:
        repo, repo_df = pull_read(DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data",
                                      DATA_FILE = os.path.join("data", DATA_FILENAME),
                                      HF_TOKEN = "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")
        repo.git_pull()
                    
        if str(repo_df["ogrenci_no"][0]) == password:
            st.write("Giriş başarılı")       
            answer_code = st.radio(
            "Cevap Anahtari Kodu",
            ('1', '2', '3',"4","5"))
            answer_code = int(answer_code)      
            global myIndexs 
                        
            image = Image.open(image_file)
            image = np.array(image.convert('RGB'))
                    #(ans_txt,pathImage, save_images= True)
            resim_list,myIndexs =reader.reader(pathImage=image,save_images=False) 
              
            #myIndex1_str =", ".join(map(str, myIndexs[0]))
            st.write("Ders 1 icin cevap anahtari")
            df = pd.DataFrame(
    [
       {"Sorular": "Soru1 ", "Cevap": myIndexs[0][0],"Sorular2": "Soru11 ", "Cevap6": myIndexs[0][10]},
       {"Sorular": "Soru2", "Cevap": myIndexs[0][1],"Sorular2": "Soru12 ", "Cevap6": myIndexs[0][11]},
       {"Sorular": "Soru3", "Cevap": myIndexs[0][2],"Sorular2": "Soru13 ", "Cevap6": myIndexs[0][12]},
       {"Sorular": "Soru4 ", "Cevap": myIndexs[0][3],"Sorular2": "Soru14 ", "Cevap6": myIndexs[0][13]},
       {"Sorular": "Soru5", "Cevap": myIndexs[0][4],"Sorular2": "Soru15 ", "Cevap6": myIndexs[0][14]},
       {"Sorular": "Soru6 ", "Cevap": myIndexs[0][5],"Sorular2": "Soru16 ", "Cevap6": myIndexs[0][15]},
       {"Sorular": "Soru7", "Cevap": myIndexs[0][6],"Sorular2": "Soru17 ", "Cevap6": myIndexs[0][16]},
       {"Sorular": "Soru8", "Cevap": myIndexs[0][7],"Sorular2": "Soru18 ", "Cevap6": myIndexs[0][17]},
       {"Sorular": "Soru9 ", "Cevap": myIndexs[0][8],"Sorular2": "Soru19 ", "Cevap6": myIndexs[0][18]},
       {"Sorular": "Soru10", "Cevap": myIndexs[0][9],"Sorular2": "Soru20 ", "Cevap6": myIndexs[0][19]}
   ]
)
            edited_df = st.experimental_data_editor(df,use_container_width=True,height=400)
            
 
      
            if st.button("Kaydet"):
                        repo, repo_df = pull_read(DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data",
                                      DATA_FILE = os.path.join("data", DATA_FILENAME),
                                      HF_TOKEN = "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")
                        repo.git_pull()
                
                        image = Image.open(image_file)
                        image = np.array(image.convert('RGB'))
                #(ans_txt,pathImage, save_images= True)
                        
                        myIndex1_str =", ".join(map(str, edited_df["Cevap"]))
                        myIndex2_str =", ".join(map(str, myIndexs[1]))
                        myIndex3_str =", ".join(map(str, myIndexs[2]))
                        #new_data1 = pd.DataFrame(data, index, columns)
                        data = [[1,answer_code,80,myIndex1_str,90,myIndex2_str,10,myIndex3_str]]
  
# Create the pandas DataFrame
                        new_data = pd.DataFrame(data, columns=['sinav_kodu', 'ogrenci_no',
                                                         "notu1","yanlis_sorulari1",
                                                         "notu2","yanlis_sorulari2",
                                                         "notu3","yanlis_sorulari3"])
                        
                        repo_df = repo_df[repo_df['ogrenci_no'] != answer_code]
                    

                        updated = update(new_data=new_data,ex_df=repo_df)
                #st.dataframe(updated,use_container_width=True)
                        save_and_push(dataFrame=updated,repo=repo,fileName=f"data/{DATA_FILENAME}")
            
                        #st.download_button(label="Tum verileri indirmek icin tiklayin",data=convert_df_to_csv(updated),
                         #      file_name=f'{teacher_code}.csv',mime='text/csv',)      
        else:
            st.write("Giris basarisiz kontrol ediniz.")            
            
#python -m streamlit run app.py
if __name__ == '__main__':
    screen_scan_main()	   