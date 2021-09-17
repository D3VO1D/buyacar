export const isValidUSZipCode = (zipCode) => /(^\d{5}$)|(^\d{5}-\d{4}$)/.test(zipCode);
