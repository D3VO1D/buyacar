import { State, City } from 'country-state-city';

export const getStatesCities = () => {
    const states = State.getStatesOfCountry('US');
    const cities = City.getCitiesOfCountry('US');
    return [...states, ...cities];
};
