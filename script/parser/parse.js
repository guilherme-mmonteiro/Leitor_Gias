'use strict';

const { PdfReader } = require('pdfreader');

function readPDFPages(buffer, reader = (new PdfReader())) {

  return new Promise((resolve, reject) => {
    let pages = [];
    reader.parseBuffer(buffer, (err, item) => {

      if (err)
        reject(err)

      else if (!item)
        resolve(pages);

      else if (item.page)
        pages.push({});

      else if (item.text) {
        const row = pages[pages.length - 1][item.y] || [];
        row.push(item.text);
        pages[pages.length - 1][item.y] = row;
      }

    });
  });
}


function parseBill(pages) {

  const page = pages[0]; 
  const fields = {

    nome_empresa: { row: '10.375', index: 0 },
    mes: { row: '8.25', index: 1 },
    suporte: { row: '29.234', index: 1 },
    valor_contabil: { row: '29.234', index: 2 },
    valor_base_calculo: { row: '29.234', index: 3 },
    debito_icms: { row: '31.328000000000003', index: 0 },

  };
  

  const data = {};

  Object.keys(fields)
    .forEach((key) => {

      const field = fields[key];
      const val = page[field.row][field.index];

      data[key] = val;

    });

    if (data.valor_base_calculo == null) {
      data.valor_base_calculo = data.valor_contabil
      data.valor_contabil = data.suporte 
    }

  return data;

}

module.exports = async function parse(buf, reader) {

  const data = await readPDFPages(buf, reader);
  //console.log({'beforeParse': data});

  const parsedData = parseBill(data);
  // return data;
  return parsedData;

};