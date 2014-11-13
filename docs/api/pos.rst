Pos
----


Web Interface for Mobile Client
+++++++++++++++++++++++++++++++



.. http:get:: /publishers

   This request asks for the list of all publishers possessed by the requested POS.

   **Example request**:

   .. sourcecode:: http

      GET /publishers HTTP/1.1
      Host: pos_host.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "publisher_id": '12345',
          "publisher_name": 'sinica',
          "publisher_desc": "This POS located in Academic Sinica."
        },
        {
          "publisher_id": '12346',
          "publisher_name": 'city_hall_711',
          "publisher_desc": "This POS located in 7-11 near city hall."
        }
      ]

   :query offset: offset number. default is 0
   :query limit: limit number. default is 30
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no user


.. ----------------------------------------


.. http:get:: /topics/(str:publisher_id)

   This request asks for the list of all topics belonged to the publisher, identified as `publisher_id`.

   **Example request**:

   .. sourcecode:: http

      GET /topics/12345 HTTP/1.1
      Host: pos_host.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "topic_id": 't0005',
          "topic_name": 'shelters',
          "topic_desc": "This topic is about shelters nearby.",
          "accountibility_name": "email_certification"
        },
        {
          "topic_id": 't0056',
          "topic_name": 'buildings',
          "topic_desc": "This topic is about buildings nearby.",
          "accountibility_name": "phone_certification"
        },
      ]

   :query offset: offset number. default is 0
   :query limit: limit number. default is 30

   :reqheader Authorization: optional OAuth token to authenticate

   :statuscode 200: no error
   :statuscode 404: there's no publisher identified as (publisher_id)



.. http:get:: /data_verify/(str:publisher_id)/(str:topic_id)

   This request ask for the permission of a specific topic, identified as (`publisher_id`)/(`topic_id`). If the accountability is established, a `data_key` is returned for accessing the topic

   **Example request**:

   .. sourcecode:: http

      GET /data_verify/12345/t0056 HTTP/1.1
      Host: pos_host.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
        "status": 'success',
        "data_size": '500kb',
        "data_key": 'docatsinicaiis',
        "key_valid_time": "2014/05/06:03:31"
      }
        


   :reqheader Authorization: optional OAuth token to authenticate

   :statuscode 200: no error
   :statuscode 404: there's no topic identified as (topic_id)@(publisher_id)



.. http:get:: /data_request/(str:data_key)

   The request is used to get the topic's access path (in terms of URL) by giving the corresponding `data_key`. 

   **Example request**:

   .. sourcecode:: http

      GET /data_request/docatsinicaiis HTTP/1.1
      Host: pos_host.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
        "status": 'success',
        "data_request_url": '/data/sdfasdfasfaweqfgeraaf'

      }
        


   :reqheader Authorization: optional OAuth token to authenticate

   :statuscode 200: no error
   :statuscode 404: invalid data_key