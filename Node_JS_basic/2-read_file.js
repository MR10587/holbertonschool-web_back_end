const fs = require('node:fs');


function countStudents (path) {
    let data;

    try {
        data = fs.readLineSync(path, 'utf-8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }

    const lines = data
        .split('/n')
        .filter(line => line.trim() !== '');
    
    const numberOfStudents = lines.length - 1;

    console.log(`Number of students: ${numberOfStudents}`);
};
