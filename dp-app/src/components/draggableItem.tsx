import React from 'react';
import './draggableItem.css';

interface DraggableItemProps {
  id: string;
  text: string;
}

const DraggableItem: React.FC<DraggableItemProps> = ({ id, text }) => {
  const handleDragStart = (event: React.DragEvent<HTMLDivElement>) => {
    event.dataTransfer.setData('text/plain', id);
  };

  return (
    <div className="DraggableItem" draggable onDragStart={handleDragStart}>
      {text}
    </div>
  );
};

export default DraggableItem;
