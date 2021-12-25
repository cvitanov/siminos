#http://stackoverflow.com/questions/6183479/cropping-a-pdf-using-ghostscript-9-01
pdfcrop kstwsspred.pdf kstwsspred.pdf
gs \
  -o BudCvi-kssspred.pdf \
  -sDEVICE=pdfwrite \
  -c "[/CropBox [40 0 389 294] /PAGES pdfmark" \
  -f kstwsspred.pdf
