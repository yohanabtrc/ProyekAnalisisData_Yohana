# ProyekAnalisisData_Yohana
Proyek Analisis Data - Dicoding 2024

Tahap Analisa yang dilakukan:
1. Menentukan pertanyaan bisnis:
- Pertanyaan 1: Bagaimana demografi pelanggan yang dimiliki oleh perusahaan? #customer_dataset.csv
- Pertanyaan 2: Bagaimana performa penjualan perusahaan dalam beberapa waktu belakangan?

2. Import library yang digunakan
3. Data Wrangling
   a. Gathering data
    - import data dari google drive dengan perintah ! gdown --id linkdataset
   
   b. Assesing Data
    - melakukan pemeriksaaan terkait dataset yang digunakan
    - .info()
      terdapat kolom yaitu order_approved_at dan order_delivered_carrier_date yang sebelumnya masih bertipe object diubah   
      menjadi datetime
    - memeriksa apakah ada kolom yang terdapat bagian kosong (.isna().sum())
    - memeriksa apakah terdapat dataset yang terindikasi terduplikasi
    - .describe()
   
   c. Cleaning Data
    - menghapus duplikasi
    - melakukan drop terhadap baris yang terdapat data kosong
    - memeriksa apakah masih ada dataset yang terdapat data kosong/null
4. Exploratory Data Analysis (EDA)
   - Explore data dari masing-masing dataset
   - melakukan merge pada dataset
   - melakukan .groupby
5. Visualization & Explanatory Analysis
   - Bagaimana demografo pelanggan yang dimiliki oleh perusahaan : melakukan visualisasi dengan bar chart
   - Bagaimana performa penjualan dalam beberapa waktu belakangan : melakukan visualisasi dengan bar chart berdasarkan 
     penjualan tiap bulannya.

Conclusion:
Conclution pertanyaan 1: Berdasarkan demografi, dari seluruh kota asal customer, didapatkan hasil bahwa 10 kota dengan   tingkat penjualan tertinggi adalah san paulo, rio de janiero, belo harizonte. brasilia, curitiba, campinas, portoo alegre, salvador, guarulhos, san bernardo da campo.

Conclution pertanyaan 2: Berdasarkan data dan hasil visualisasi, didapatkan hasil bahwa performa penjualan dalam beberapa waktu belakangan, bulan dengan penjualan tertinggi adalah pada bulan 11 tahun 2017. Produk dengan penjualan tertinggi adalah produk dengan kode aca2eb7d00ea1a7b8ebd4e68314663af dengan penjualan sebanyak 520 dan yang terendah adalah produk dengan id 00066f42aeeb9f3007548bb9d3f33c38 dengan banyak penjualan 1.
