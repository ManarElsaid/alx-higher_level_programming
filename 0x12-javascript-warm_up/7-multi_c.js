#!/usr/bin/node

const argc = Number(process.argv[2]);
if (isNaN(argc)) { console.log('Missing number of occurrences'); } for (let i = 0; i < argc; i++) { console.log('C is fun'); }
