'use client';
import React from 'react';
import {useDropzone} from 'react-dropzone';

const FileUploader = () => {
  const { getRootProps, getInputProps, acceptedFiles } = useDropzone();
  
  const files = acceptedFiles.map((file: File) => (
    <li key={file.name}>
      {file.name} - {file.size} bytes
    </li>
  ));

  return (
    <section className="flex flex-col items-center justify-center p-4 w-full h-4/5">
      <div {...getRootProps({className: 'dropzone container flex flex-col items-center justify-center p-6 border-4 border-dashed border-gray-200 bg-dark rounded-lg h-full w-full md:w-2/3 lg:w-1/2'})}>
        <input {...getInputProps()} type="file"/>
        <p className='text-white-500 font-medium'>Drag 'n' drop a document here, or click to select files</p>
      </div>
      <aside className="w-full md:w-2/3 lg:w-1/2">
        <h4 className="text-lg font-semibold mb-4">Files</h4>
        <ul className="list-disc pl-5">{files}</ul>
      </aside>
    </section>
  );
}

export default FileUploader;
