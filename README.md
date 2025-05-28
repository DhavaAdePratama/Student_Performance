# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya jaya institut adalah sebuah institusi pendidikan yang telah berdiri lama sejak tahun 2000. institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. namun masih banyak juga mahasiswa yang terkena dropout. jumlah dropout yang cukup tinggi ini merupakan suatu masalah besar bagi institusi ini.

### Permasalahan Bisnis
Tingkat dropout mahasiswa yang tinggi menjadi tantangan serius bagi institusi pendidikan, tidak hanya berdampak pada reputasi akademik tetapi juga pada efektivitas operasional dan keberlanjutan institusi itu sendiri. Fenomena ini mengindikasikan perlunya upaya preventif yang berbasis data guna mengidentifikasi mahasiswa yang berisiko tinggi untuk keluar dari sistem pendidikan sebelum waktunya.

Jaya Jaya Institut menyadari pentingnya intervensi dini dan berinisiatif untuk mengembangkan sistem prediktif yang mampu mendeteksi potensi dropout sejak dini. Dengan pendekatan ini, institusi berharap dapat memberikan pendampingan dan bimbingan yang lebih tepat sasaran bagi mahasiswa yang membutuhkan, sekaligus meningkatkan tingkat retensi dan keberhasilan akademik secara keseluruhan.


### Cakupan Proyek

1. Data Understanding 

    - Memahami struktur data mahasiswa yang mencakup informasi terkait demografi, kualifikasi orang tua, data keuangan, serta performa nya dalam mengikuti pemebelajaran di seemester 1 dan 2.

2. Data Preprocessing 

    - Mencari insight data 
    - normalisasi fitur numerik serta mengencoding label target (status)
    - split dataset menajdi 90% train dan 10%data test
    - penyeimbangan data menggunakan metode oversampling 

3. Modeling

    - Model yang digunakan dalam eksperimen ini adalah Gradient Boosting classifier serta juga menggunakan Hyper-parameter tuning yaitu GridSearch 

    - Model Pembanding: Decision Tree, Random Forest, 

4. Evaluasi Model 

    - Confusion Matrix

    - Classification Report (Accuracy, Precision, Recall, F1-Score)



### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment: 
Clone repository ini ke komputer lokal yang anda miliki : ``` Git clone https://github.com/DhavaAdePratama/Student_Performance ```

Set Up PYTHON sesuai requirements yang ada  : ``` pip install -r requirements.txt ```

## Business Dashboard

Link Dashboard : https://public.tableau.com/app/profile/dhava.ade.pratama/viz/DASHBOARD_17468711608590/Dashboard1?publish=yes

Berdasarkan Dashboard yang telah dibuat, tidak terdapat perbandingan yang siginifikan pada latar pendidikan orang tua mahasiswa, namun jika dilihat dalam performa akademik pada semester 1 mahsiswa yang dropout cenderung tidak lulus dalam mata kuliah yang diambil, begitupun di semster 2 kejadian tersebut juga terulang kembali, di lain sisi mahasiswa yang dropout memiliki rata rata umur yang lebih tua dibandingkan dengan mahasiswa dengan status lainnya, selain itu mahasiswa dropout juga banyak yang tidak tepat waktu / memiliki tunggakan dalam melakukan pembayaran.
 

## Menjalankan Sistem Machine Learning

Link Akses prototype: https://studentperformance-nufzluii8mbdkmnb2aw9cz.streamlit.app/

cara menjalankan nya donwload dulu requirements nya ``` https://github.com/DhavaAdePratama/Student_Performance/blob/main/requirements.txt```

kemudian download satu folder modul model ```https://github.com/DhavaAdePratama/Student_Performance/tree/main/model```

setelah itu donwload semua file pada modul app ```https://github.com/DhavaAdePratama/Student_Performance/tree/main/app```

running secara bergantian file pada modul app pada environment masing masing dimulai dari data preprocessing kemudian app dan terakhir Student_performance nya 

setelah berhasil di running silahkan bukan command prompt dan arahkan ke tempat file direktory di tempat anda menaruh file ini dan terakhir ketik ``` streamlit run Student_Performace.py ```
 
## Conclusion

berdasarkan hasil analisis  dapat disimpulkan bahwa terdapat pola-pola tertentu yang menunjukkan kecenderungan mahasiswa untuk mengalami dropout. Salah satu temuan utama adalah bahwa mahasiswa yang mengalami dropout umumnya memiliki performa akademik yang rendah, khususnya pada dua semester pertama. Mereka cenderung tidak lulus dalam sebagian besar mata kuliah yang diambil, yang menunjukkan bahwa kesulitan belajar sejak awal perkuliahan merupakan indikator penting terhadap risiko dropout.

Selain itu, usia saat mendaftar kuliah juga menjadi faktor yang cukup mencolok. Mahasiswa yang dropout rata-rata memiliki usia yang lebih tua dibandingkan dengan mahasiswa lainnya yang masih aktif atau telah lulus. Hal ini bisa jadi menunjukkan adanya tekanan atau tanggung jawab eksternal di luar dunia akademik, seperti pekerjaan atau tanggungan keluarga, yang berpotensi menghambat kelancaran studi mereka.

Aspek finansial juga muncul sebagai faktor penting. Data menunjukkan bahwa banyak mahasiswa yang mengalami dropout memiliki riwayat keterlambatan atau ketidakteraturan dalam pembayaran biaya kuliah. Kondisi ini mencerminkan adanya kendala ekonomi yang dapat memperberat beban mahasiswa, sehingga mereka lebih rentan untuk keluar dari sistem pendidikan.

### Rekomendasi Action Items

- Memonitoring serta memberikan pengarahan terhadap mahasiswa di semseter semester awal, seperti memberikan tips & trick agar mendapatkan IPK yang bagus, dll.

- mengcrosscheck data setiap mahasiswa agar mahasiswa mahasiswa yang tidak mampu dapat mendapatkan bantuan biaya pendidikan.

- memberikan workshop/seminar mengenai (akademik, keuangan,kewirausahaan) kepada mahasiswa agar memiliki pikiran pikiran yang lebih maju dalam bidang akademik dan keungan.



