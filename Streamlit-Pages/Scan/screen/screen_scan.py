import csv
import streamlit as st
import numpy as np
import cv2
from PIL import Image
import optic1
from functions import image_show
import pandas as pd 
from data_func import make_new_data,update,save_and_push
import os
from huggingface_hub import Repository
import reader

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
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
    password = st.text_input("Şifre:",key=17,type="password")
    
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
                
            exam_code = st.text_input("Sınav Kodu:",key=13,value=10)

            exam_code = int(exam_code)
                
            global myIndexs 
            try:
                if myIndexs == None:
                    st.write("Cevap Anahtari Yok")

                else:
                    st.write("Cevap Anahtari Secili")
                
            except NameError:
                st.write("Cevap Anahtari Yok")
                
            answer_code = st.radio(
            "Cevap Anahtari Kodu",
                ('1', '2', '3',"4","5"))
            
            if st.button("Cevap Anahtari Sec",key=51):
                global cevap1_list 
                global cevap2_list 
                global cevap3_list
                cevap1_list = []
                cevap2_list = []
                cevap3_list = []
                
                answer_code = int(answer_code)
                repo_df_filt = repo_df[repo_df['ogrenci_no'] == answer_code]
                cevap1= repo_df_filt["yanlis_sorulari1"]
                cevap2= repo_df_filt["yanlis_sorulari2"]   
                cevap3= repo_df_filt["yanlis_sorulari3"]
                

                for veri in cevap1:
                    parcalar = veri.split(",")  # Veriyi "," ile ayırın
                    parcalar_int = [int(parca) for parca in parcalar]  # Parçaları integer'a dönüştürün
                    cevap1_list.extend(parcalar_int)  # Parçaları veri_listesi'ne ekleyin
                for veri in cevap2:
                    parcalar = veri.split(",")  # Veriyi "," ile ayırın
                    parcalar_int = [int(parca) for parca in parcalar]  # Parçaları integer'a dönüştürün
                    cevap2_list.extend(parcalar_int)  # Parçaları veri_listesi'ne ekleyin
                for veri in cevap3:
                    parcalar = veri.split(",")  # Veriyi "," ile ayırın
                    parcalar_int = [int(parca) for parca in parcalar]  # Parçaları integer'a dönüştürün
                    cevap3_list.extend(parcalar_int)  # Parçaları veri_listesi'ne ekleyin
                
            col3,col4 = st.columns(2)
            with col3:
            
                if st.button("Tara ve Sonucu Goruntule",key=52):
                
                        image = Image.open(image_file)
                        image = np.array(image.convert('RGB'))
                #(ans_txt,pathImage, save_images= True)
                        grading, wrong_ans, student_idFix, resim_list,empty_ans =optic1.optic1(ans_txt1=cevap1_list,
                                                                             ans_txt2=cevap2_list,
                                                                             ans_txt3=cevap3_list,
                                                                             pathImage=image,save_images=False) 
            
                #image_show(resim_list)
                        if len(wrong_ans[0]) == 0:
                            wrong_ans[0] = "0"
                        wrong_ans_str = (str(wrong_ans[0]))
                        st.write("Ogrenci Numarasi:",student_idFix)
                        st.write("Ders1 Yanlis Yaptigi sorular:",(str(wrong_ans[0])))
                        st.write("Ders1 Bos Yaptigi sorular:",(str(empty_ans[0])))
                        st.write("Ders1 Notu:",int(grading[0]))
                        st.write("Ders2 Yanlis Yaptigi sorular:",(str(wrong_ans[1])))
                        st.write("Ders2 Bos Yaptigi sorular:",(str(empty_ans[1])))
                        st.write("Ders2 Notu:",int(grading[1]))
                        st.write("Ders3 Yanlis Yaptigi sorular:",(str(wrong_ans[2])))
                        st.write("Ders3 Bos Yaptigi sorular:",(str(empty_ans[2])))
                        st.write("Ders3 Notu:",int(grading[2]))
        
            with col4:
                if st.button("Tara ve Sonucu Kaydet"):
                        repo, repo_df = pull_read(DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data",
                                      DATA_FILE = os.path.join("data", DATA_FILENAME),
                                      HF_TOKEN = "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")
                        repo.git_pull()
                
                        image = Image.open(image_file)
                        image = np.array(image.convert('RGB'))
                #(ans_txt,pathImage, save_images= True)
                        grading, wrong_ans, student_idFix, resim_list =optic1.optic1(ans_txt1="cevapanahtari/cevapanahtari_ders1.txt",
                                                                             ans_txt2="cevapanahtari/cevapanahtari_ders2.txt",
                                                                             ans_txt3="cevapanahtari/cevapanahtari_ders3.txt",
                                                                             pathImage=image,save_images=False) 
            
                #image_show(resim_list)
                        if len(wrong_ans[0]) == 0:
                            wrong_ans[0] = "0"
#
                        wrong_ans_str = (str(wrong_ans[0]))
                        new_data = make_new_data(sinav_kodu=exam_code, ogrenci_no=int(student_idFix),
                        notu=int(grading[0]),yanlislar=str(wrong_ans_str))
            
                #st.dataframe(new_data)
                        updated = update(new_data=new_data,ex_df=repo_df)
                #st.dataframe(updated,use_container_width=True)
                        save_and_push(dataFrame=updated,repo=repo,fileName=f"data/{DATA_FILENAME}")
            
                        st.download_button(label="Tum verileri indirmek icin tiklayin",data=convert_df_to_csv(updated),
                               file_name=f'{teacher_code}.csv',mime='text/csv',)      
        else:
            st.write("Giris basarisiz kontrol ediniz.")            
            
#python -m streamlit run app.py
if __name__ == '__main__':
    screen_scan_main()	   