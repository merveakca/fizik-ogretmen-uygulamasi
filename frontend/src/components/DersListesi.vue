<template>
    <div class="container">
      <h1>Ders Listesi</h1>
      <ul class="ders-listesi">
        <li v-for="ders in dersler" :key="ders.id" class="ders-item">
          {{ ders.ad }} - {{ ders.aciklama }}
          <button @click="dersSil(ders.id)" class="btn-sil">Sil</button>
          <button @click="dersiDüzenle(ders)" class="btn-guncelle">Güncelle</button>
        </li>
      </ul>
  
      <h2>{{ düzenlenenDers ? "Ders Güncelle" : "Ders Ekle" }}</h2>
      <form @submit.prevent="düzenlenenDers ? dersGuncelle() : dersEkle()" class="ders-form">
        <input v-model="yeniDers.ad" placeholder="Ders Adı" class="input" />
        <input v-model="yeniDers.aciklama" placeholder="Ders Açıklaması" class="input" />
        <button type="submit" class="btn">{{ düzenlenenDers ? "Güncelle" : "Ekle" }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dersler: [],
        yeniDers: {
          ad: '',
          aciklama: ''
        },
        düzenlenenDers: null,  // Güncelleme işlemi için seçilen ders
      };
    },
    mounted() {
      this.dersleriYukle();
    },
    methods: {
      dersleriYukle() {
        axios.get('http://127.0.0.1:8000/api/dersler/')
          .then(response => {
            this.dersler = response.data;
          })
          .catch(error => {
            console.error('API hatası:', error);
          });
      },
      dersEkle() {
        axios.post('http://127.0.0.1:8000/api/dersler/', this.yeniDers)
          .then(() => {
            this.dersler.push({ ...this.yeniDers });  // Yeni dersi listeye ekle
            this.yeniDers.ad = '';
            this.yeniDers.aciklama = '';
          })
          .catch(error => {
            console.error('API hatası:', error);
          });
      },
      dersSil(id) {
        axios.delete(`http://127.0.0.1:8000/api/dersler/${id}/`)
          .then(() => {
            this.dersler = this.dersler.filter(ders => ders.id !== id);
          })
          .catch(error => {
            console.error('API hatası:', error);
          });
      },
      dersiDüzenle(ders) {
        this.düzenlenenDers = ders;  // Güncellenecek dersi seç
        this.yeniDers.ad = ders.ad;
        this.yeniDers.aciklama = ders.aciklama;
      },
      dersGuncelle() {
        axios.put(`http://127.0.0.1:8000/api/dersler/${this.düzenlenenDers.id}/`, this.yeniDers)
          .then(() => {
            const index = this.dersler.findIndex(d => d.id === this.düzenlenenDers.id);
            this.dersler[index] = { ...this.yeniDers };  // Güncellenen dersi listede güncelle
            this.yeniDers.ad = '';
            this.yeniDers.aciklama = '';
            this.düzenlenenDers = null;  // Güncelleme işlemi bittiğinde sıfırla
          })
          .catch(error => {
            console.error('API hatası:', error);
          });
      }
    }
  }
  </script>
  
  <style>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  h1, h2 {
    color: #333;
    text-align: center;
  }
  
  .ders-listesi {
    list-style-type: none;
    padding: 0;
  }
  
  .ders-item {
    background-color: #f9f9f9;
    margin: 10px 0;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .ders-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .input {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .btn {
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .btn:hover {
    background-color: #218838;
  }
  
  .btn-sil {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .btn-sil:hover {
    background-color: #c82333;
  }
  
  .btn-guncelle {
    background-color: #ffc107;
    color: black;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
    margin-left: 5px;
  }
  
  .btn-guncelle:hover {
    background-color: #e0a800;
  }
  </style>
  