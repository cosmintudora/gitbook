import React from 'react';
import { RedocStandalone } from 'redoc';

export default function ApiDocs() {
    return <RedocStandalone specUrl="/openapi.yaml" />;
}