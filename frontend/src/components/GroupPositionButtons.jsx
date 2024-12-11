import React from 'react';
import { Button, Flex } from 'antd';
const GroupPositionButtons = () => (
  <Flex  gap="large" wrap>
    <Button type="primary" danger>Удалить выбранное</Button>
    <Button type="primary">Добавить группу</Button>
  </Flex>
);
export default GroupPositionButtons;