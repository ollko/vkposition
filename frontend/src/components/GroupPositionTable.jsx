import React, { useState } from 'react';
import { Space, Table, Button } from 'antd';


const columns = [
    {
        title: 'группа',
        dataIndex: 'group',
        key: 'group',
        render: (text) => <a>{text}</a>,
    },
    {
        title: 'количество участников',
        dataIndex: 'group_count',
        key: 'group_count',
    },
    {
        title: 'средняя позиция',
        dataIndex: 'avg_position',
        key: 'avg_position',
    },
    {
        title: 'динамика',
        key: 'dynamic',
        dataIndex: 'dynamic',
    },
    {
        title: 'топ 10/11-30/31-100',
        key: 'top',
        dataIndex: 'top',
    },
    {
        title: 'ключевые запросы',
        key: 'group_url',
        dataIndex: 'group_url',
        render: (text) => <Button type="link"link={{text}}>запросы</Button>,
    },
];
const dataSource = [
    {   key: '1',
        group: 'ёжики',
        group_count: 100,
        avg_position: 2,
        dynamic: '+0 =6 -0',
        top: '0 13 0',
        group_url: 'ya.ru'
    },
    {
        key: '2',
        group: 'овцы',
        group_count: 100,
        avg_position: 2,
        dynamic: '+0 =6 -0',
        top: '0 13 0',
        group_url: 'ya.ru'
    },
    {
        key: '3',
        group: 'крокодилы',
        group_count: 100,
        avg_position: 2,
        dynamic: '+0 =6 -0',
        top: '0 13 0',
        group_url: 'ya.ru'
    },
];
const GroupPositionTable = () => {
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const onSelectChange = (newSelectedRowKeys) => {
      console.log('selectedRowKeys changed: ', newSelectedRowKeys);
      setSelectedRowKeys(newSelectedRowKeys);
    };
    const rowSelection = {
        selectedRowKeys,
        onChange: onSelectChange,
        selections: [
            Table.SELECTION_ALL,
            Table.SELECTION_INVERT,
            Table.SELECTION_NONE,
        ],
    };
    return <Table rowSelection={rowSelection} columns={columns} dataSource={dataSource} />;
  };


export default GroupPositionTable;