import React from 'react';
import './dragDropContainer.css';

interface DragDropContainerProps {
  children: React.ReactNode;
}

const DragDropContainer: React.FC<DragDropContainerProps> = ({ children }) => {
  const handleDrop = (event: React.DragEvent<HTMLDivElement>) => {
    // Handle the drop logic here
  };

  const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
  };

  return (
    <div className="DragDropContainer" onDrop={handleDrop} onDragOver={handleDragOver}>
      {children}
    </div>
  );
};

export default DragDropContainer;
