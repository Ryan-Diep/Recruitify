import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AudioUpload from './components/AudioUpload';
import { useNavigate } from 'react-router-dom';

const Results: React.FC = () => {
  const [pitch, setPitch] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string>('');
  const [isUploading, setIsUploading] = useState(false);
  const navigate = useNavigate();
  
  const handleAudioChange = (file: File) => {
    setAudioFile(file);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!audioFile) {
      setStatus('Please fill in all entries');
      return;
    }

    const formData = new FormData();
    if (audioFile) formData.append('audio', audioFile);

    setIsUploading(true);
    setStatus('Uploading...');

    try {
      const response = await axios.post('/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setStatus(response.data.message || 'Upload successful!');
      
      setAudioFile(null);
    } catch (error) {
      console.error('Error:', error);
      setStatus('Upload failed. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };

  useEffect(() => {
    const fetchPitch = async () => {
      try {
        const response = await axios.get('http://localhost:5000/generate-pitch');
        console.log("API Response:", response.data); 
        setPitch(response.data.pitch);
      } catch (error) {
        console.error('Error fetching pitch:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPitch();
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-2xl">
        <h1 className="text-2xl font-bold mb-6 text-center text-black">Generated Pitch</h1>
        {loading ? (
          <p className="text-center text-gray-500">Loading...</p>
        ) : (
          <p className="text-gray-800 whitespace-pre-line">{pitch}</p>
        )}
        <form onSubmit={handleSubmit} className="space-y-6">
          <AudioUpload onFileChange={handleAudioChange} />
          <button
            type="submit"
            onClick={() => navigate('/Video')}
            disabled={isUploading || (!audioFile)}
            className={`w-full py-2 px-4 rounded-lg transition-colors ${
              isUploading || (!audioFile)
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
        <button onClick={() => navigate('/')} className="mt-6 w-full py-2 px-4 bg-blue-500 text-white rounded-lg">
          Upload Another File
        </button>
      </div>
    </div>
  );
};

export default Results;