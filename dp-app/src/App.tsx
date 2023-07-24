import React from 'react';
import DragDropContainer from './components/dragDropContainer';
import DraggableItem from './components/draggableItem';

const App: React.FC = () => {
  return (
    <div className="App">
      <DragDropContainer>
        <div className="Row">
          <div className="Column">
            <DraggableItem id="item1" text="Draggable Item 1" />
          </div>
          <div className="Column">
            <DraggableItem id="item2" text="Draggable Item 2" />
          </div>
        </div>
        <div className="Row">
          <div className="Column">
            <DraggableItem id="item3" text="Draggable Item 3" />
          </div>
          <div className="Column">
            <DraggableItem id="item4" text="Draggable Item 4" />
          </div>
        </div>
      </DragDropContainer>
    </div>
  );
};

export default App;
