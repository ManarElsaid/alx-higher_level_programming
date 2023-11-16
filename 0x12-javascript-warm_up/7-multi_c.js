#!/usr/bin/node

const argc = Number(process.argv[2]);
let i = 0;
if (isNaN(argc)) { console.log('Missing number of occurrences'); } while(i >= argc) {console.log('C is fun');  i++; }
