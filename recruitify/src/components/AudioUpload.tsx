import React, { useState } from 'react';

interface AudioUploadProps {
  onFileChange: (file: File) => void;
}

const AudioUpload: React.FC<AudioUploadProps> = ({ onFileChange }) => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      onFileChange(selectedFile); // Pass the file to the parent component
    }
  };

  return (
    <div className="mb-6">
      <label htmlFor="audioUpload" className="block text-sm font-medium text-gray-700 mb-2">
        Upload Audio:
      </label>
      <div className="flex items-center">
        <input
          type="file"
          id="audioUpload"
          accept="audio/*"
          onChange={handleFileChange}
          className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />
      </div>
      {file && <p className="mt-2 text-sm text-gray-600">Selected Audio: {file.name}</p>}
    </div>
  );
};

export default AudioUpload;
