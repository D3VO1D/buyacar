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

    getCars(page = 1) {
        return this.apiClient.get(`/api/v1/cars?page=${page}`);
    }
}

export const API = new Api();
