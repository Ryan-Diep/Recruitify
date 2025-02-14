import React, { useState } from 'react';
import axios from 'axios';
import PdfUpload from './components/PdfUpload';
import VideoUpload from './components/VideoUpload';
import './App.css';

const App: React.FC = () => {
  const [pdfFile, setPdfFile] = useState<File | null>(null);
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string>('');
  const [isUploading, setIsUploading] = useState(false);

  const handlePdfChange = (file: File) => {
    setPdfFile(file);
  };

  const handleVideoChange = (file: File) => {
    setVideoFile(file);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!pdfFile && !videoFile) {
      setStatus('Please upload at least one file (PDF or video).');
      return;
    }

    const formData = new FormData();
    if (pdfFile) formData.append('pdf', pdfFile);
    if (videoFile) formData.append('video', videoFile);

    setIsUploading(true);
    setStatus('Uploading...');

    try {
      const response = await axios.post('/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setStatus(response.data.message || 'Upload successful!');
      
      setPdfFile(null);
      setVideoFile(null);
    } catch (error) {
      console.error('Error:', error);
      setStatus('Upload failed. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Upload Your Files</h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          <PdfUpload onFileChange={handlePdfChange} />
          <VideoUpload onFileChange={handleVideoChange} />
          <button
            type="submit"
            disabled={isUploading || (!pdfFile && !videoFile)}
            className={`w-full py-2 px-4 rounded-lg transition-colors ${
              isUploading || (!pdfFile && !videoFile)
                ? 'bg-gray-400 cursor-not-allowed'
                : 'bg-blue-500 hover:bg-blue-600 text-white'
            }`}
          >
            {isUploading ? 'Uploading...' : 'Upload'}
          </button>
        </form>
        {status && (
          <p className={`mt-4 text-center ${
            status.includes('success') ? 'text-green-500' : 
            status === 'Uploading...' ? 'text-blue-500' : 'text-red-500'
          }`}>
            {status}
          </p>
        )}
      </div>
    </div>
  );
};

export default App;