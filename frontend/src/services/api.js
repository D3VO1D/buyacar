import axios from 'axios';

const DEFAULT_API_URL = 'http://localhost:8000';

class Api {
    constructor() {
        this.apiClient = axios.create({
            baseURL: process.env.VUE_APP_API_URL || DEFAULT_API_URL,
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
        });
    }

    getCars(page = 1, filtersQuery = '') {
        return this.apiClient.get(`/api/v1/cars?page=${page}&${filtersQuery}`);
    }

    getMinYear() {
        return this.apiClient.get('/api/v1/min_year');
    }

    getUserCity() {
        return this.apiClient.get('/api/v1/usercity');
    }

    getMakes() {
        return this.apiClient.get('/api/v1/makes');
    }
}

export const getPlacesForZIP = (zipCode) => axios.get(`https://api.zippopotam.us/us/${zipCode}`, {
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
});

export const API = new Api();
