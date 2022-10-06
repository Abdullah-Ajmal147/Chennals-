from argparse import ArgumentParser
import contextlib
import PyPDF2


def main():
    ap = ArgumentParser(
        description='Combines several PDF files into one file.')

    # The files to combine
    ap.add_argument('files', metavar='file1 file2 ...',
                    help='Files to combine', nargs='+')

    # The output file (defaults to combined.pdf if not specified)
    ap.add_argument('-o', '--output', nargs='?',
                    const='combined.pdf', default='combined.pdf',
                    help='Output file name (combined.pfd, if not specified)')

    args = ap.parse_args()

    # Workaround for PyPDF2 empty output file: keep input files open
    # See https://stackoverflow.com/a/49927541/336802
    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        files = [stack.enter_context(open(pdf, 'rb')) for pdf in args.files]
        for f in files:
            pdfMerger.append(f)
        with open(args.output, 'wb') as f:
            pdfMerger.write(f)

if __name__ == '__main__':
    main()
# import glob
# from PyPDF2 import PdfFileMerger

# def merger(output_path, input_paths):
#     pdf_merger = PdfFileMerger()
#     file_handles = []
    
#     for path in input_paths:
#         pdf_merger.append(path)
        
#     with open(output_path, 'wb') as fileobj:
#         pdf_merger.write(fileobj)
        
# if __name__ == '__main__':
#     paths = glob.glob('*.pdf')
#     paths.sort()
#     merger('output.pdf', paths)