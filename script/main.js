const glob = require('glob');
const fs = require('fs');

glob("script/data/*.pdf", (error, filesWithPDF)=>{

  // if(error){
  //   console.log(error)
  // }
  // console.log(filesWithPDF);

  const executar = `lista = ['${filesWithPDF.join(`', '`)}']`

    fs.writeFile('script/lista.py', executar, (err) => {
        if(err) throw err;
        console.log("----------------- lista criada -----------------");
    });

 })