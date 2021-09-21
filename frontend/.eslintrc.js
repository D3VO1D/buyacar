module.exports = {
    root: true,
    env: {
        browser: true,
        node: true,
    },
    extends: [
        'plugin:vue/essential',
        '@vue/airbnb',
    ],
    parserOptions: {
        parser: 'babel-eslint',
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-plusplus': 'off',
        quotes: [
            'error',
            'single',
        ],
        semi: [
            'error',
            'always',
        ],
        indent: [
            'error',
            4,
        ],
        'max-len': [
            'error',
            120,
            2,
            {
                ignoreUrls: true,
                ignoreComments: true,
                ignoreRegExpLiterals: true,
                ignoreStrings: false,
                ignoreTemplateLiterals: false,
            },
        ],
        'import/extensions': ['error', 'always', {
            js: 'never',
            mjs: 'never',
            vue: 'never',
        }],
        'import/prefer-default-export': 'off',
    },
};
