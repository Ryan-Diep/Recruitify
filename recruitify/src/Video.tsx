import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Results: React.FC = () => {
  const [pitch, setPitch] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const navigate = useNavigate();

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
        <h1 className="text-2xl font-bold mb-6 text-center text-black">Generated Video</h1>
        {/* {loading ? (
          <p className="text-center text-gray-500">Loading...</p>
        ) : (
          <p className="text-gray-800 whitespace-pre-line">{pitch}</p>
        )} */}
        <button onClick={() => navigate('/')} className="mt-6 w-full py-2 px-4 bg-blue-500 text-white rounded-lg">
          Upload Another File
        </button>
      </div>
    </div>
  );
};

export default Results;