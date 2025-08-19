# Cloudfare R2 Setup

Cloudflare R2 – a S3-compatible object storage service with no egress fees, ideal for use as a Snowflake external stage.
Store Parquet, CSV, or JSON files and use COPY INTO or external tables without worrying about high data transfer costs.
Supports secure access via access keys and integrates easily with Snowflake for analytics and data pipelines.

## Setup

1. [Sign up](https://dash.cloudflare.com/sign-up) to create your account.

2. Go to **R2 Object Storage** and add your payment information.
![img02](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img02.png)

3. Select **+ Create bucket**.
![img03](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img03.png)

4. Add a **bucket name** and select **Create Bucket**.
![img04](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img04.png)

5. Go back to **R2 Object Storage** and select **{} API** and then **Manage API tokens**.
![img05](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img05.png)

6. Select **Create Account API token**.
![img06](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img06.png)

7. Set the parameters according to your needs and select **Create Account API token**.
![img07](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img07.png)

8. You will get the **Secret Access Key** and **Access Key ID** to create an external stage in Snowflake.
![img08](https://github.com/aldoruizw/codelab/blob/main/Cloudfare/img/img08.png)

9. You can create a stage in Snowflake.
```bash
CREATE STAGE ANALYTICS.PUBLIC.STAGE_R2
    URL = ' s3compat://yourbucket/'
    ENDPOINT = 'ABCD.r2.cloudflarestorage.com'
    CREDENTIALS = ( AWS_KEY_ID = 'yourkeyid'
                    AWS_SECRET_KEY = 'yoursecretkey');
```

---

©️ Powered by [Cloudfare](https://www.cloudflare.com/)
